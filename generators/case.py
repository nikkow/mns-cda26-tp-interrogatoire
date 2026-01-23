from typing import List, Literal
from pydantic import BaseModel, Field

CASE_SYSTEM_PROMPT = """
Vous êtes un générateur d'affaires criminelles pour un jeu d'interrogatoire.
Vous devez produire UNIQUEMENT un JSON valide, sans texte autour.

Contraintes de contenu :
- Langue : français
- Pas de contenu sexuel, pas de violence graphique, pas de descriptions macabres
- Affaires autorisées : vol, escroquerie, sabotage, meurtre (sans détails)
- L'affaire doit être jouable en interrogatoire : le suspect a une défense plausible mais contient 2 à 4 contradictions exploitables

Exigences :
- Le JSON doit respecter EXACTEMENT le schéma fourni.
- Toutes les chaînes doivent être non vides.
- Les heures doivent être au format "HH:MM".
"""

CASE_USER_PROMPT = """
Générez une affaire originale pour un interrogatoire.
Le suspect doit avoir :
- une version officielle (son histoire)
- la vérité (ce qu'il s'est réellement passé)
- une liste de mensonges ou omissions
- 2 à 4 contradictions possibles à déclencher par questions (heures, lieux, objets, relations, alibi)

Retournez **UNIQUEMENT** le JSON conforme au schéma.
"""


class Setting(BaseModel):
    city: str
    place: str
    date: str
    time_window: str


class Suspect(BaseModel):
    name: str
    age: int = Field(ge=18, le=80)
    job: str
    temperament: str
    goal: str


class TimelineClaim(BaseModel):
    time: str
    claim: str


class OfficialStory(BaseModel):
    summary: str
    timeline: List[TimelineClaim] = Field(min_length=3)


class TimelineFact(BaseModel):
    time: str
    fact: str


class Truth(BaseModel):
    summary: str
    timeline: List[TimelineFact] = Field(min_length=3)
    motive: str


class ContradictionHook(BaseModel):
    trigger_topic: str
    what_suspect_claims: str
    what_is_true: str
    how_to_corner: str


class SuspectBehaviorRules(BaseModel):
    style: str
    never_do: List[str] = Field(min_length=3)
    allowed_moves: List[str] = Field(min_length=3)


class Case(BaseModel):
    case_id: str
    crime_type: Literal["vol", "escroquerie", "sabotage", "meurtre"]
    title: str
    setting: Setting
    suspect: Suspect
    official_story: OfficialStory
    truth: Truth
    evidence_known_to_police: List[str] = Field(min_length=2)
    lies_or_omissions: List[str] = Field(min_length=2)
    contradiction_hooks: List[ContradictionHook] = Field(min_length=2, max_length=4)
    suspect_behavior_rules: SuspectBehaviorRules
