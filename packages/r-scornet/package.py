# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScornet(RPackage):
	"""Semi-Supervised Calibration of Risk with Noisy Event Times

	A consistent, semi-supervised, non-parametric survival curve estimator optimized for efficient use of Electronic Health Record (EHR) data with a limited number of current status labels. See van der Laan and Robins (1997) <doi:10.2307/2670119>.
	"""
	
	homepage = "https://github.com/celehs/SCORNET"
	cran = "SCORNET" 

	version("0.1.1", md5="76e086476ae0359029631fe98b8050a3")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
