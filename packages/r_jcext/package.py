# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJcext(RPackage):
	"""Extended Classification of Weather Types

	Provides a gridded classification of weather types by applying the Jenkinson and Collison classification. For a given region (it can be either local region or the whole map),it computes at each grid the 11 weather 
             types during the period considered for the analysis. See Otero et al., (2017) <doi:10.1007/s00382-017-3705-y> for more information.
	"""
	
	cran = "jcext" 

	version("0.1.1", md5="1e295f16d058f45deda4ecb3adf3cda3")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rworldmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
