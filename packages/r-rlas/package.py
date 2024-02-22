# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlas(RPackage):
	"""Read and Write 'las' and 'laz' Binary File Formats Used for
Remote Sensing Data

	Read and write 'las' and 'laz' binary file formats. The LAS file format is a public file format for the interchange of 3-dimensional point cloud data between data users. The LAS specifications are approved by the American Society for Photogrammetry and Remote Sensing <https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities>. The LAZ file format is an open and lossless compression scheme for binary LAS format versions 1.0 to 1.4 <https://laszip.org/>.
	"""
	
	homepage = "https://github.com/r-lidar/rlas"
	cran = "rlas" 

	version("1.7.0", md5="4ff01e8caa362feba512e381d51339a3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
