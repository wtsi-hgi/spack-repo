# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZlog(RPackage):
	"""Z(log) Transformation for Laboratory Measurements

	Transformation of laboratory measurements into z or z(log)-value
    based on given or empirical reference limits as proposed in
    Hoffmann et al. 2017 <doi:10.1515/labmed-2016-0087>.
	"""
	
	homepage = "https://github.com/ampel-leipzig/zlog/"
	cran = "zlog" 

	version("1.0.2", md5="197282401f07eb9bcde77379526f4a54")

	depends_on("r@3.6:", type=("build", "run"))
