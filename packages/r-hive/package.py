# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHive(RPackage):
	"""Hadoop InteractiVE

	Hadoop InteractiVE facilitates distributed 
             computing via the MapReduce paradigm through R and Hadoop. An easy to use 
             interface to Hadoop, the Hadoop Distributed File System (HDFS), 
	     and Hadoop Streaming is provided.
	"""
	
	cran = "hive" 

	version("0.2-2", md5="2481c9069575cc1caaee80ae96ea3e41")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-rjava@0.9.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("hadoop@2.7.2:", type=("build", "link", "run"))
