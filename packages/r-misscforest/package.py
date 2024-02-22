# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisscforest(RPackage):
	"""Ensemble Conditional Trees for Missing Data Imputation

	Single imputation based on the Ensemble Conditional Trees (i.e. Cforest algorithm Strobl, C., Boulesteix, A. L., Zeileis, A., & Hothorn, T. (2007) <doi:10.1186/1471-2105-8-25>). 
	"""
	
	homepage = "https://github.com/ielbadisy/missCforest"
	cran = "missCforest" 

	version("0.0.8", md5="8878ee4e64a637ded4ea51c6b82af197")

	depends_on("r-partykit", type=("build", "run"))
