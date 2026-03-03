# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataspacer(RPackage):
	"""Interface to 'the CAVD DataSpace'

	Provides a convenient API interface to access immunological data
    within 'the CAVD DataSpace'(<https://dataspace.cavd.org>), a data sharing 
    and discovery tool that facilitates exploration of HIV immunological data 
    from pre-clinical and clinical HIV vaccine studies.
	"""
	
	homepage = "https://docs.ropensci.org/DataSpaceR/"
	cran = "DataSpaceR" 

	version("0.7.6", md5="b52c38d807e91dfafd93d7f8e1bf9971")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlabkey@2.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
