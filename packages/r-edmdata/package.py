# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdmdata(RPackage):
	"""Data Sets for Psychometric Modeling

	Collection of data sets from various assessments that can be used to 
    evaluate psychometric models. These data sets have been analyzed in the
    following papers that introduced new methodology as part of the application section:
    Yinghan Chen et al. (2021) <doi:10.1007/s11336-021-09750-9>,
    Yinyin Chen et al. (2020) <doi:10.1007/s11336-019-09693-2>,
    Culpepper, S. A. (2019a) <doi:10.1007/s11336-019-09683-4>,
    Culpepper, S. A. (2019b) <doi:10.1007/s11336-018-9643-8>,
    Culpepper, S. A., & Chen, Y. (2019) <doi:10.3102/1076998618791306>,
    Culpepper, S. A., & Balamuta, J. J. (2017) <doi:10.1007/s11336-015-9484-7>,
    and Culpepper, S. A. (2015) <doi:10.3102/1076998615595403>.
	"""
	
	homepage = "https://tmsalab.github.io/edmdata/"
	cran = "edmdata" 

	version("1.2.0", md5="459c834573f812a110140c4ea9906431")

	depends_on("r@3.5:", type=("build", "run"))
