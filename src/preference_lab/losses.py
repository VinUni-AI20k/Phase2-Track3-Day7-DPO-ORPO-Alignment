from __future__ import annotations
import numpy as np

def dpo_loss(policy_chosen_logps: np.ndarray, policy_rejected_logps: np.ndarray, ref_chosen_logps: np.ndarray, ref_rejected_logps: np.ndarray, beta: float) -> float:
    """Compute batch DPO loss from sequence log probabilities.

    TODO(student): implement numerically stable DPO loss.
    Hint: compare policy log-ratio against reference log-ratio, then use log-sigmoid.
    """
    raise NotImplementedError("TODO(student): implement DPO loss")

def orpo_loss(sft_nll: np.ndarray, chosen_logps: np.ndarray, rejected_logps: np.ndarray, lambda_orpo: float) -> float:
    """Compute a simplified ORPO-style objective.

    TODO(student): implement SFT loss + odds-ratio preference penalty.
    """
    raise NotImplementedError("TODO(student): implement ORPO loss")
