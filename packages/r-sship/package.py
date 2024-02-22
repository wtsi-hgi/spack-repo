# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSship(RPackage):
	"""Tool for Secure Shipment of Content

	Convenient tools for exchanging files securely from within R. By
    encrypting the content safe passage of files (shipment) can be provided by
    common but insecure carriers such as ftp and email. Based on asymmetric
    cryptography no management of shared secrets is needed to make a secure
    shipment as long as authentic public keys are available. Public keys used
    for secure shipments may also be obtained from external providers as part of
    the overall process. Transportation of files will require that relevant
    services such as ftp and email servers are available.
	"""
	
	homepage = "https://github.com/Rapporteket/sship"
	cran = "sship" 

	version("0.9.0", md5="1c0247315020544b348d0989e1e98d5b")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
