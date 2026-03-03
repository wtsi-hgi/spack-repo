# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbfs(RPackage):
	"""Initial Basic Feasible Solution for Transportation Problem

	The initial basic feasible solution (IBFS) is a significant step to achieve the minimal total cost (optimal solution) of the transportation problem. However, the existing methods of IBFS do not always provide a good feasible solution which can reduce the number of iterations to find the optimal solution. This initial basic feasible solution can be obtained by using any of the following methods. 
             a) North West Corner Method. 
             b) Least Cost Method. 
             c) Row Minimum Method. 
             d) Column Minimum Method. 
             e) Vogel's Approximation Method.
             etc.
             For more technical details about the algorithms please refer below URLs.
             <https://theintactone.com/2018/05/24/ds-u2-topic-8-transportation-problems-initial-basic-feasible-solution/>.
             <https://www.brainkart.com/article/Methods-of-finding-initial-Basic-Feasible-Solutions_39037/>.
             <https://myhomeworkhelp.com/row-minima-method/>.
             <https://myhomeworkhelp.com/column-minima-method/>.
	"""
	
	cran = "IBFS" 

	version("1.0.0", md5="4316142bf7d5b319696b5b18161871b6")

