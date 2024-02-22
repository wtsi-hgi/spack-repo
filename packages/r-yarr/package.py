# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYarr(RPackage):
	"""Yet Another 'ARFF' Reader

	A parser and a writer for 'WEKA' Attribute-Relation File Format
    <https://waikato.github.io/weka-wiki/arff_stable/> in pure R, with no dependencies. 
    As opposed to other R implementations, this package can read standard
    (dense) as well as sparse files, i.e. those where each row does only contain 
    nonzero components. Unlike 'RWeka', 'yarr' does not require any 'Java' installation
    nor is dependent on external software. This implementation is generalized from 
    those in packages 'mldr' and 'mldr.datasets'.
	"""
	
	homepage = "https://github.com/fdavidcl/yarr"
	cran = "yarr" 

	version("0.1.2", md5="c4ac569f126afdedaa51e50ae047a4e0")

	depends_on("r@3.6:", type=("build", "run"))
