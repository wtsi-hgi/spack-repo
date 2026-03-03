# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmvl(RPackage):
	"""Mappable Vector Library for Handling Large Datasets

	Mappable vector library provides convenient way to access large datasets. Use all of your data at once, with few limits. Memory mapped data can be shared between multiple R processes. Access speed depends on storage medium, so solid state drive is recommended, preferably with PCI Express (or M.2 nvme) interface or a fast network file system. The data is memory mapped into R and then accessed using usual R list and array subscription operators. Convenience functions are provided for merging, grouping and indexing large vectors and data.frames. The layout of underlying MVL files is optimized for large datasets. The vectors are stored to guarantee alignment for vector intrinsics after memory map. The package is built on top of libMVL, which can be used as a standalone C library. libMVL has simple C API making it easy to interchange datasets with outside programs. Large MVL datasets are distributed via Academic Torrents <https://academictorrents.com/collection/mvl-datasets>. 
	"""
	
	homepage = "https://academictorrents.com/collection/mvl-datasets"
	cran = "RMVL" 

	version("1.0.0.1", md5="76245156f867ecf16e9b7cda4901f13a")

	depends_on("r@3.5:", type=("build", "run"))
