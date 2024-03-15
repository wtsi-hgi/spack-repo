# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvmover(RPackage):
	"""Read and Write Data

	Offers a wide range of functions for reading and writing data in various file formats, 
    including CSV, RDS, Excel and ZIP files. 
    Additionally, it provides functions for retrieving metadata associated with files, 
    such as file size and creation date, making it easy to manage and organize large data sets. 
    This package is designed to simplify data import and export tasks, 
    and provide users with a comprehensive set of tools to work with different types of data files.
	"""
	
	homepage = "https://vusaverse.github.io/vvmover/"
	cran = "vvmover" 

	version("1.6.0", md5="399db5903440f8e41318f7d5793c5ee2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
