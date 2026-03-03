# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetpack(RPackage):
	"""Density Estimation and Random Number Generation with
Distribution Element Trees

	Density estimation for possibly large data sets and conditional/unconditional random number generation or bootstrapping with distribution element trees. The function 'det.construct' translates a dataset into a distribution element tree. To evaluate the probability density based on a previously computed tree at arbitrary query points, the function 'det.query' is available. The functions 'det1' and 'det2' provide density estimation and plotting for one- and two-dimensional datasets. Conditional/unconditional smooth bootstrapping from an available distribution element tree can be performed by 'det.rnd'. For more details on distribution element trees, see: Meyer, D.W. (2016) <arXiv:1610.00345> or Meyer, D.W., Statistics and Computing (2017) <doi:10.1007/s11222-017-9751-9> and Meyer, D.W. (2017) <arXiv:1711.04632> or Meyer, D.W., Journal of Computational and Graphical Statistics (2018) <doi:10.1080/10618600.2018.1482768>.
	"""
	
	cran = "detpack" 

	version("1.1.3", md5="3fa158608d8cc5ee9cbd26f17954ab88")

