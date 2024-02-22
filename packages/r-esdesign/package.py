# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsdesign(RPackage):
	"""Adaptive Enrichment Designs with Sample Size Re-Estimation

	Software of 'esDesign' is developed to implement the adaptive 
    enrichment designs with sample size re-estimation presented in 
    Lin et al. (2021) <doi: 10.1016/j.cct.2020.106216>. In details, 
    three-proposed trial designs are provided, including the AED1-SSR (or ES1-SSR),
    AED2-SSR (or ES2-SSR) and AED3-SSR (or ES3-SSR). In addition, this package 
    also contains several widely used adaptive designs, such as the Marker 
    Sequential Test (MaST) design proposed Freidlin et al. 
    (2014) <doi:10.1177/1740774513503739>, the adaptive enrichment designs 
    without early stopping (AED or ES), the sample size re-estimation 
    procedure (SSR) based on the conditional power proposed by 
    Proschan and Hunsberger (1995), and some useful functions. 
    In details, we can calculate the futility and/or efficacy stopping 
    boundaries, the sample size required, calibrate the value of the threshold 
    of the difference between subgroup-specific test statistics, conduct the 
    simulation studies in AED, SSR, AED1-SSR, AED2-SSR and AED3-SSR.
	"""
	
	cran = "esDesign" 

	version("1.0.3", md5="5ecc790dc3517a1d4eefa740680742e2")

	depends_on("r@3.2:", type=("build", "run"))
