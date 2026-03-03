# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAzurekusto(RPackage):
	"""Interface to 'Kusto'/'Azure Data Explorer'

	An interface to 'Azure Data Explorer', also known as 'Kusto', a fast, distributed data exploration service from Microsoft: <https://azure.microsoft.com/en-us/products/data-explorer/>. Includes 'DBI' and 'dplyr' interfaces, with the latter modelled after the 'dbplyr' package, whereby queries are translated from R into the native 'KQL' query language and executed lazily. On the admin side, the package extends the object framework provided by 'AzureRMR' to support creation and deletion of databases, and management of database principals. Part of the 'AzureR' family of packages.
	"""
	
	homepage = "https://github.com/Azure/AzureKusto"
	cran = "AzureKusto" 

	version("1.1.3", md5="31b33eaf828bcaec989e52a889fc9456")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-azureauth", type=("build", "run"))
	depends_on("r-azurermr@2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@0.2.4:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
