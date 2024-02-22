# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfacebookstat(RPackage):
	"""Load Data from Facebook API Marketing

	Load data by campaigns, ads, ad sets and insights, ad account and business manager 
    from Facebook Marketing API into R. For more details see official documents by Facebook 
    Marketing API <https://developers.facebook.com/docs/marketing-apis/>.
	"""
	
	homepage = "https://selesnow.github.io/rfacebookstat/"
	cran = "rfacebookstat" 

	version("2.10.0", md5="cbe49cfb851887a6b5ad16baac63ac04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
