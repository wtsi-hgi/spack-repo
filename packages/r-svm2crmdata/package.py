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

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="0ed46f3c6bc459d098f5a95555003f1192b4604a0734d077370863d6a792eccc")

	depends_on("r@3.2:", type=("build", "run"))

