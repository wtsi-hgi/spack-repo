# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNzpullover(RPackage):
	"""Driving Offences in New Zealand Between 2009 and 2016

	Datasets of driving offences and fines in New Zealand between 2009 and 2017.
    Originally published by the New Zealand Police at
    <http://www.police.govt.nz/about-us/publication/road-policing-driver-offence-data-january-2009-december-2017>.
	"""
	
	homepage = "https://github.com/nacnudus/nzpullover"
	cran = "nzpullover" 

	version("0.3.0", md5="d24c8dee3886e034979ad778e7e98ac9")

	depends_on("r@3.2.5:", type=("build", "run"))
