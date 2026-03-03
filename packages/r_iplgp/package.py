# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIplgp(RPackage):
	"""Identification of Parental Lines via Genomic Prediction

	
    Combining genomic prediction with Monte Carlo simulation, three different 
    strategies are implemented to select parental lines for multiple traits in plant 
    breeding. The selection strategies include (i) GEBV-O considers only genomic 
    estimated breeding values (GEBVs) of the candidate individuals; (ii) GD-O 
    considers only genomic diversity (GD) of the candidate individuals; and (iii) 
    GEBV-GD considers both GEBV and GD. The above method can be seen in Chung PY, 
    Liao CT (2020) <doi:10.1371/journal.pone.0243159>. Multi-trait genomic best 
    linear unbiased prediction (MT-GBLUP) model is used to simultaneously estimate 
    GEBVs of the target traits, and then a selection index is adopted to evaluate 
    the composite performance of an individual.
	"""
	
	homepage = "https://github.com/py-chung/IPLGP"
	cran = "IPLGP" 

	version("2.0.4", md5="0f313aafcea94377eface3355844fdff")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sommer", type=("build", "run"))
