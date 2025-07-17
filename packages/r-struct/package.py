# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStruct(RPackage):
    """Statistics in R Using Class-based Templates

    Defines and includes a set of class-based templates for developing and implementing data processing and analysis workflows, with a strong emphasis on statistics and machine learning. The templates can be used and where needed extended to 'wrap' tools and methods from other packages into a common standardised structure to allow for effective and fast integration. Model objects can be combined into sequences, and sequences nested in iterators using overloaded operators to simplify and improve readability of the code. Ontology lookup has been integrated and implemented to provide standardised definitions for methods, inputs and outputs wrapped using the class-based templates.
    """

    bioc = "struct"

    version("1.20.1", commit="0d4f5fd044a6fe4699b2ccc2d61501ec205052c6")
    version("1.14.1", commit="03769d217e45c72604cb4e151b69212559249c96")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ontologyindex", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rols@2.30.1:", type=("build", "run"))
