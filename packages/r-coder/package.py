# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoder(RPackage):
	"""Deterministic Categorization of Items Based on External Code
Data

	
  Fast categorization of items based on external code data identified by 
  regular expressions. A typical use case considers patient with medically coded 
  data, such as codes from the International Classification of Diseases ('ICD') or 
  the Anatomic Therapeutic Chemical ('ATC') classification system. 
  Functions of the package relies on a triad of objects: (1) case data with unit 
  id:s and possible dates of interest; (2) external code data for corresponding 
  units in (1) and with optional dates of interest and; (3) a classification 
  scheme ('classcodes' object) with regular expressions to identify and 
  categorize relevant codes from (2). 
  It is easy to introduce new classification schemes ('classcodes' objects) or  
  to use default schemes included in the package. Use cases includes patient 
  categorization based on 'comorbidity indices' such as 'Charlson', 'Elixhauser', 
  'RxRisk V', or the 'comorbidity-polypharmacy' score (CPS), as well as adverse 
  events after hip and knee replacement surgery.
	"""
	
	homepage = "https://docs.ropensci.org/coder/"
	cran = "coder" 

	version("0.13.10", md5="b94df3ae83b68dc2c39650a711fe1571")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-decoder", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
