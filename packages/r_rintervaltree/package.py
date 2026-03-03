# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRintervaltree(RPackage):
	"""An Interval Tree Tool for Real Numbers

	This tool can be used to build binary interval trees using real number inputs. 
    The tree supports queries of intervals overlapping a single number or an interval (start, end). 
    Intervals with same bounds but different names are treated as distinct intervals. 
    Insertion of intervals is also allowed. Deletion of intervals is not implemented at this point.
    See  Mark de Berg, Otfried Cheong, Marc van Kreveld, Mark Overmars (2008). Computational Geometry: Algorithms and Applications, for a reference.
	"""
	
	cran = "rIntervalTree" 

	version("0.1.0", md5="8e6d3d90147c555253763bef44ca6e04")

