# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGformula(RPackage):
	"""Parametric G-Formula

	Implements the parametric g-formula algorithm of Robins (1986) 
    <doi:10.1016/0270-0255(86)90088-6>. The g-formula can be used to estimate 
    the causal effects of hypothetical time-varying treatment interventions on 
    the mean or risk of an outcome from longitudinal data with time-varying 
    confounding. This package allows: 1) binary or continuous/multi-level 
    time-varying treatments; 2) different types of outcomes (survival or 
    continuous/binary end of follow-up); 3) data with competing events or 
    truncation by death and loss to follow-up and other types of censoring 
    events; 4) different options for handling competing events in the case of 
    survival outcomes; 5) a random measurement/visit process; 6) joint 
    interventions on multiple treatments; and 7) general incorporation of a 
    priori knowledge of the data structure.
	"""
	
	homepage = "https://github.com/CausalInference/gfoRmula"
	cran = "gfoRmula" 

	version("1.0.4", md5="46ffaae4e026db5edd70ebb830da8e24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-truncreg", type=("build", "run"))
