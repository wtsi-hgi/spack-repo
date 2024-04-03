# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaltoolboxdp(RPackage):
	"""Data Pre-Processing Extensions

	An important aspect of data analytics is related to data management support for artificial intelligence. It is related to preparing data correctly. This package provides extensions to support data preparation in terms of both data sampling and data engineering. Overall, the package provides researchers with a comprehensive set of functionalities for data science based on experiment lines, promoting ease of use, extensibility, and integration with various tools and libraries. Information on Experiment Line is based on Ogasawara et al. (2009) <doi:10.1007/978-3-642-02279-1_20>.
	"""
	
	homepage = "https://github.com/cefet-rj-dal/daltoolboxdp"
	cran = "daltoolboxdp" 

	version("1.0.767", md5="17aafe65a4b8731b4d90581c42eef96a")

	depends_on("r-daltoolbox", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-fselector", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-smotefamily", type=("build", "run"))
