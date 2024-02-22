# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApfr(RPackage):
	"""Multiple Testing Approach using Average Power Function (APF) and
Bayes FDR Robust Estimation

	Implements a multiple testing approach to the
    choice of a threshold gamma on the p-values using the
    Average Power Function (APF) and Bayes False Discovery
    Rate (FDR) robust estimation. Function apf_fdr() 
    estimates both quantities from either raw data or
    p-values. Function apf_plot() produces smooth graphs 
    and tables of the relevant results. Details of the methods
    can be found in Quatto P, Margaritella N, et al. (2019) 
    <doi:10.1177/0962280219844288>.
	"""
	
	cran = "APFr" 

	version("1.0.2", md5="8c445cfcd85c074af52b62fcce92905b")

	depends_on("r@3.5:", type=("build", "run"))
