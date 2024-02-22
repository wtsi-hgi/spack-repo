# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComorbidity(RPackage):
	"""Computing Comorbidity Scores

	Computing comorbidity indices and scores such as the weighted Charlson
  score (Charlson, 1987 <doi:10.1016/0021-9681(87)90171-8>) and the Elixhauser
  comorbidity score (Elixhauser, 1998 <doi:10.1097/00005650-199801000-00004>)
  using ICD-9-CM or ICD-10 codes (Quan, 2005 <doi:10.1097/01.mlr.0000182534.19832.83>).
  Australian and Swedish modifications of the Charlson Comorbidity Index are available
  as well (Sundararajan, 2004 <doi:10.1016/j.jclinepi.2004.03.012> and Ludvigsson, 2021 
  <doi:10.2147/CLEP.S282475>), together with different weighting algorithms for both
  the Charlson and Elixhauser comorbidity scores.
	"""
	
	homepage = "https://ellessenne.github.io/comorbidity/"
	cran = "comorbidity" 

	version("1.0.7", md5="74cdc8be616b712b002ca63b9281c389")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
