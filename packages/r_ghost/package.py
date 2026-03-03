# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhost(RPackage):
	"""Missing Data Segments Imputation in Multivariate Streams

	Helper functions provide an accurate imputation algorithm for reconstructing the missing segment in a multi-variate data streams. Inspired by single-shot learning, it reconstructs the missing segment by identifying the first similar segment in the stream. Nevertheless, there should be one column of data available, i.e. a constraint column. The values of columns can be characters (A, B, C, etc.). The result of the imputed dataset will be returned a .csv file. For more details see Reza Rawassizadeh (2019) <doi:10.1109/TKDE.2019.2914653>.
	"""
	
	homepage = "https://www.researchgate.net/publication/332779980_Ghost_Imputation_Accurately_Reconstructing_Missing_Data_of_the_Off_Period"
	cran = "Ghost" 

	version("0.1.0", md5="fd17aa324b6fa9607cd8dae7a91ca504")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
