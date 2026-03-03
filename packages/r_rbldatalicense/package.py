# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbldatalicense(RPackage):
	"""R Interface to 'Bloomberg Data License'

	R interface to access prices and market data with the 
    'Bloomberg Data License' service from 
    <https://www.bloomberg.com/professional/product/data-license/>. 
    As a prerequisite, a valid Data License from 'Bloomberg' is needed 
    together with the corresponding SFTP credentials and whitelisting 
    of the IP from which accessing the service. 
    This software and its author are in no way affiliated, 
    endorsed, or approved by 'Bloomberg' or any of its affiliates.
    'Bloomberg' is a registered trademark.
	"""
	
	homepage = "https://rbldatalicense.eguidotti.com"
	cran = "RblDataLicense" 

	version("0.2.5", md5="be36001b66ca51fdea7ea5915215fbfc")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
