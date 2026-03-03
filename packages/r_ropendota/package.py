# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopendota(RPackage):
	"""Access OpenDota Services in R

	Provides a client for the API of OpenDota. OpenDota is a web service which is provide DOTA2 real time data. Data is collected through the Steam WebAPI. With ROpenDota you can easily grab the latest DOTA2 statistics in R programming such as latest match on official international competition, analyzing your or enemy performance to learn their strategies,etc. Please see <https://github.com/rosdyana/ROpenDota> for more information.
	"""
	
	homepage = "https://github.com/rosdyana/ROpenDota"
	cran = "ROpenDota" 

	version("0.1.2", md5="3b1522ce7ec66b5c49526b4823bb4991")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
