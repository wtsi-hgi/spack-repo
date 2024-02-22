# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibulltools(RPackage):
	"""Statistical Methods for Life Data Analysis

	Provides statistical methods and visualizations that are often 
             used in reliability engineering. Comprises a compact and easily 
             accessible set of methods and visualization tools that make the 
             examination and adjustment as well as the analysis and interpretation 
             of field data (and bench tests) as simple as possible.
             Non-parametric estimators like Median Ranks, 
             Kaplan-Meier (Abernethy, 2006, <ISBN:978-0-9653062-3-2>), 
             Johnson (Johnson, 1964, <ISBN:978-0444403223>), and Nelson-Aalen 
             for failure probability estimation within samples that contain 
             failures as well as censored data are included.   
             The package supports methods like Maximum Likelihood and Rank Regression, 
             (Genschel and Meeker, 2010, <DOI:10.1080/08982112.2010.503447>) 
             for the estimation of multiple parametric lifetime distributions,  
             as well as the computation of confidence intervals of quantiles and 
             probabilities using the delta method related to Fisher's confidence 
             intervals (Meeker and Escobar, 1998, <ISBN:9780471673279>) and the 
             beta-binomial confidence bounds. 
             If desired, mixture model analysis can be done with segmented regression
             and the EM algorithm.
             Besides the well-known Weibull analysis, the package also contains 
             Monte Carlo methods for the correction and completion of imprecisely 
             recorded or unknown lifetime characteristics.
             (Verband der Automobilindustrie e.V. (VDA), 2016, <ISSN:0943-9412>). 
             Plots are created statically ('ggplot2') or interactively ('plotly') and 
             can be customized with functions of the respective visualization package.
             The graphical technique of probability plotting as well as the addition 
             of regression lines and confidence bounds to existing plots are 
             supported. 
	"""
	
	homepage = "https://tim-tu.github.io/weibulltools/"
	cran = "weibulltools" 

	version("2.1.0", md5="3226ba4c456b13488ce70c1a5f0e2ede")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@0.12.18:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
