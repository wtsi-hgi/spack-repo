# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynergyfinder(RPackage):
    """Calculate and Visualize Synergy Scores for Drug Combinations

    Efficient implementations for analyzing pre-clinical multiple drug combination datasets. It provides efficient implementations for 1.the popular synergy scoring models, including HSA, Loewe, Bliss, and ZIP to quantify the degree of drug combination synergy; 2. higher order drug combination data analysis and synergy landscape visualization for unlimited number of drugs in a combination; 3. statistical analysis of drug combination synergy and sensitivity with confidence intervals and p-values; 4. synergy barometer for harmonizing multiple synergy scoring methods to provide a consensus metric of synergy; 5. evaluation of synergy and sensitivity simultaneously to provide an unbiased interpretation of the clinical potential of the drug combinations. Based on this package, we also provide a web application (http://www.synergyfinder.org) for users who prefer graphical user interface.
    """

    homepage = "http://www.synergyfinder.org"
    bioc = "synergyfinder"

    version("3.16.0", commit="ba995e744d0522595205a53451c293658dc29492")
    version("3.10.3", commit="90ba7b94c23d0560e8759dde2e7c3e2fd81bbb7c")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-drc@3.0.1:", type=("build", "run"))
    depends_on("r-reshape2@1.4.4:", type=("build", "run"))
    depends_on("r-tidyverse@1.3:", type=("build", "run"))
    depends_on("r-dplyr@1.0.3:", type=("build", "run"))
    depends_on("r-tidyr@1.1.2:", type=("build", "run"))
    depends_on("r-purrr@0.3.4:", type=("build", "run"))
    depends_on("r-furrr@0.2.2:", type=("build", "run"))
    depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
    depends_on("r-ggforce@0.3.2:", type=("build", "run"))
    depends_on("r-vegan@2.5.7:", type=("build", "run"))
    depends_on("r-gstat@2.0.6:", type=("build", "run"))
    depends_on("r-sp@1.4.5:", type=("build", "run"))
    depends_on("r-spatialextremes@2.0.9:", type=("build", "run"))
    depends_on("r-ggrepel@0.9.1:", type=("build", "run"))
    depends_on("r-kriging@1.1:", type=("build", "run"))
    depends_on("r-plotly@4.9.3:", type=("build", "run"))
    depends_on("r-stringr@1.4:", type=("build", "run"))
    depends_on("r-future@1.21:", type=("build", "run"))
    depends_on("r-mice@3.13:", type=("build", "run"))
    depends_on("r-lattice@0.20.41:", type=("build", "run"))
    depends_on("r-nleqslv@3.3.2:", type=("build", "run"))
    depends_on("r-magrittr@2.0.1:", type=("build", "run"))
    depends_on("r-pbapply@1.4.3:", type=("build", "run"))
    depends_on("r-metr@0.9.1:", type=("build", "run"))
