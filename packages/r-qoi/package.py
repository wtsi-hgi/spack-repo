# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQoi(RPackage):
	"""Read and Write QOI Images

	The new QOI file format offers a very simple but efficient image compression algorithm. This package provides an easy and simple way to read, write and display bitmap images stored in the QOI (Quite Ok Image) format. It can read and write both files and in-memory raw vectors.
	"""
	
	homepage = "https://github.com/JohannesFriedrich/qoi4R"
	cran = "qoi" 

	version("0.0.4", md5="533cfe0076c5fadc5a4c0dca5f9ef417")

	depends_on("r@2.10:", type=("build", "run"))
