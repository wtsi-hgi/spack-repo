# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmtsne(RPackage):
	"""Multiple Maps t-SNE

	An implementation of multiple maps t-distributed stochastic
    neighbor embedding (t-SNE). Multiple maps t-SNE is a method for
    projecting high-dimensional data into several low-dimensional maps such that
    non-metric space properties are better preserved than they would be by a single
    map. Multiple maps t-SNE with only one map is equivalent to standard t-SNE.
    When projecting onto more than one map, multiple maps t-SNE estimates a set
    of latent weights that allow each point to contribute to one or more maps
    depending on similarity relationships in the original data. This
    implementation is a port of the original 'Matlab' library by Laurens van der
    Maaten. 
    See Van der Maaten and Hinton (2012) <doi:10.1007/s10994-011-5273-4>.
    This material is based upon work supported by the United States Air Force 
    and Defense Advanced Research Project Agency (DARPA) under Contract No. 
    FA8750-17-C-0020.
    Any opinions, findings and conclusions or recommendations expressed in this
    material are those of the author(s) and do not necessarily reflect the views 
    of the United States Air Force and Defense Advanced Research Projects Agency.
    Distribution Statement A: Approved for Public Release; Distribution Unlimited.
	"""
	
	cran = "mmtsne" 

	version("0.1.0", md5="98f87d17079dd4d88995ab027720886a")

