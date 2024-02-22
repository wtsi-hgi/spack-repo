# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiyar(RPackage):
	"""Record Linkage and Epidemiological Case Definitions in 'R'

	An R package for iterative and batched record linkage, 
    and applying epidemiological case definitions.
    'diyar' can be used for deterministic and probabilistic record linkage, 
    or multistage record linkage combining both approaches.
    It features the implementation of nested match criteria, and mechanisms to 
    address missing data and conflicting matches during stepwise record linkage.
    Case definitions are implemented by assigning records to groups based on 
    match criteria such as person or place, and overlapping time or duration of 
    events e.g. sample collection dates or periods of hospital stays.
    Matching records are assigned a unique group ID. Index and duplicate records 
    are removed or further analyses as required.  
	"""
	
	homepage = "https://olisansonwu.github.io/diyar/index.html"
	cran = "diyar" 

	version("0.5.1", md5="152d28a305e9ff5889d4b35f53e7aa52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
