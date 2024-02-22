# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestingsimilarity(RPackage):
	"""Bootstrap Test for the Similarity of Dose Response Curves
Concerning the Maximum Absolute Deviation

	Provides a bootstrap test which decides whether two dose response curves can be assumed as equal concerning their maximum absolute deviation. A plenty of choices for the model types are available, which can be found in the 'DoseFinding' package, which is used for the fitting of the models. See <doi:10.1080/01621459.2017.1281813> for details.
	"""
	
	cran = "TestingSimilarity" 

	version("1.1", md5="d1378b84214f103701aa6dab898b8d77")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
