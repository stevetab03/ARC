"""
ARCM Position Analytics
Created by Liyuan Zhang
========================
Position-level P&L, risk attribution, and opportunity cost analysis
for the held T-bill position (CUSIP 912797UE5).

Integrates outputs from all upstream modules:
  - pipeline.py    → curve_factors.csv, position_summary.csv
  - regime.py      → regime_timeline.csv
  - dynamics.py    → regime_dynamics.csv, position_analytics.csv
  - forecast.py    → forecast_current.csv, forecast_distribution.csv

Produces a unified position report CSV for Power BI and a
printed summary suitable for daily review.

Input:
  - outputs/powerbi/position_summary.csv
  - outputs/powerbi/regime_timeline.csv
  - outputs/powerbi/regime_dynamics.csv
  - outputs/powerbi/position_analytics.csv
  - outputs/powerbi/forecast_current.csv

Output:
  - outputs/powerbi/position_report.csv
  - outputs/powerbi/scenario_analysis.csv

Usage:
  python position.py
  python position.py --purchase_price 96.439575 --purchase_date 2026-04-17
"""

import logging
import argparse
import warnings
import numpy as np
import pandas as pd

from pathlib import Path
from datetime import datetime

warnings.filterwarnings("ignore")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

#######################################
#                                     #
#    Contact me for my source code    #
#                                     #
#######################################

if __name__ == "__main__":
    main()
