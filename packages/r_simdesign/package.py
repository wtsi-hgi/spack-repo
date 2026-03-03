# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdesign(RPackage):
	"""Structure for Organizing Monte Carlo Simulation Designs

	Provides tools to safely and efficiently organize and execute 
    Monte Carlo simulation experiments in R.
    The package controls the structure and back-end of Monte Carlo simulation experiments
    by utilizing a generate-analyse-summarise workflow. The workflow safeguards against 
    common simulation coding issues, such as automatically re-simulating non-convergent results, 
    prevents inadvertently overwriting simulation files, catches error and warning messages
    during execution, and implicitly supports parallel processing.
    For a pedagogical introduction to the package see
    Sigal and Chalmers (2016) <doi:10.1080/10691898.2016.1246953>. For a more in-depth overview of 
    the package and its design philosophy see Chalmers and Adkins (2020) <doi:10.20982/tqmp.16.4.p248>.
	"""
	
	homepage = "https://github.com/philchalmers/SimDesign"
	cran = "SimDesign" 

	version("2.14", md5="a6874a180c38c31727064a90eefa69f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-pbapply@1.3.0:", type=("build", "run"))
	depends_on("r-rpushbullet", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
