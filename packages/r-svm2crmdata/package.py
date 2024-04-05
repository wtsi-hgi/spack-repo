# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvm2crmdata(RPackage):
	"""An example dataset for use with the SVM2CRM package

	An example dataset for use with the SVM2CRM package.
	"""
	
	bioc = "SVM2CRMdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SVM2CRMdata_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SVM2CRMdata/SVM2CRMdata_1.34.0.tar.gz"]

	version("1.34.0", md5="ce0c6615bfbb9a5a7cf4eeab0bd6199d")

	depends_on("r@3.2:", type=("build", "run"))

