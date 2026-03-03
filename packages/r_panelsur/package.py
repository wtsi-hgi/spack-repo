# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelsur(RPackage):
	"""Two-Way Error Component SUR Systems Estimation on Unbalanced
Panel Data

	Generalized Least Squares (GLS) estimation of Seemingly Unrelated Regression
             (SUR) systems on unbalanced panel in the one/two-way cases also taking into 
             account the possibility of cross equation restrictions.  Methodological details
             can be found in Biørn (2004) <doi:10.1016/j.jeconom.2003.10.023> and Platoni,
             Sckokai, Moro (2012) <doi:10.1080/07474938.2011.607098>.
	"""
	
	cran = "panelSUR" 

	version("0.1.0", md5="ebcafc42aad088c0ad485ec19160d38c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-matlib", type=("build", "run"))
	depends_on("r-fastmatrix", type=("build", "run"))
