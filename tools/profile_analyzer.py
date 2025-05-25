from pydantic import BaseModel
from typing import List, Optional, Dict

class Ingredient(BaseModel):
    id: str

class Nutrition(BaseModel):
    energy_kcal: Optional[float]
    energy_kj: Optional[float]
    fat: Optional[float]
    saturated_fat: Optional[float]
    carbohydrates: Optional[float]
    sugars: Optional[float]
    fiber: Optional[float]
    proteins: Optional[float]
    salt: Optional[float]
    sodium: Optional[float]

class UserProfile(BaseModel):
    allergies: List[str]
    diet: List[str]
    dislikes: List[str]
    health_goals: List[str]

class ProfileAnalyzerInput(BaseModel):
    user_profile: UserProfile
    ingredients: List[Ingredient]
    nutrition_per_100g: Nutrition

class ProfileAnalyzerOutput(BaseModel):
    score: int
    flags: List[str]
    summary: str
    explained: List[str]
    suggestion: str
    alternatives: List[Dict[str, str]]

def analyze_profile(input: ProfileAnalyzerInput) -> ProfileAnalyzerOutput:
    profile = input.user_profile
    ingr = {i.id.lower() for i in input.ingredients}
    flags = []
    explained = []

    for allergy in profile.allergies:
        if allergy.lower() in ingr:
            flags.append(f"contains_{allergy.lower()}")
            explained.append(f"Allergy: product contains {allergy}")

    if "reduce sugar" in [g.lower() for g in profile.health_goals]:
        if (input.nutrition_per_100g.sugars or 0) > 10:
            flags.append("high_sugar")
            explained.append("Sugar: above 10g not aligned with 'reduce sugar'")

    return ProfileAnalyzerOutput(
        score=85 if not flags else 65,
        flags=flags,
        summary="Scan complete. Product matched against profile.",
        explained=explained,
        suggestion="Try alternatives with less sugar or allergens.",
        alternatives=[
            { "name": "VeganBar Lite", "reason": "No milk or lecithin, only 4g sugar" },
            { "name": "Nut-Free Energy Bar", "reason": "No peanuts, low sugar, vegan certified" }
        ]
    )
