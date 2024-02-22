# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrbweaver(RPackage):
	"""Fast and Efficient Graph Data Structures

	Empower your data analysis with 'orbweaver', an R package
    designed for effortless construction and analysis of graph data
    structures. With 'orbweaver', you can seamlessly build and manipulate
    graph structures, leveraging its high-performance methods for
    filtering, joining, and mutating data within the R environment.
    Drawing inspiration from the efficiency of the 'data.table'
    package, 'orbweaver' ensures that mutations and changes to
    the graph are performed in place, streamlining your
    workflow for optimal productivity.
	"""
	
	homepage = "https://github.com/ixpantia/orbweaver"
	cran = "orbweaver" 

	version("0.0.3", md5="3fc3f0708e92e1932045c81e1d1473aa")

	depends_on("rust", type=("build", "link", "run"))
