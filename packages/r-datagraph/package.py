# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatagraph(RPackage):
	"""Export Data from 'R' to 'DataGraph'

	Functions to pipe data from 'R' to 'DataGraph', a graphing and analysis application for mac OS. Create a live connection using either '.dtable' or '.dtbin' files that can be read by 'DataGraph'. Can save a data frame, collection of data frames and sequences of data frames and individual vectors. For more information see <https://community.visualdatatools.com/datagraph/knowledge-base/r-package/>.
	"""
	
	cran = "DataGraph" 

	version("1.2.14", md5="f30a023449833b5791492541be9e0436")

	depends_on("r-rcpp", type=("build", "run"))
