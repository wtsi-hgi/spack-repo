# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestlink(RPackage):
    """NestLink an R data package to guide through Engineered Peptide Barcodes for In-Depth Analyzes of Binding Protein Ensembles

    Provides next-generation sequencing (NGS) and mass spectrometry (MS) sample data, code snippets and replication material used for developing NestLink. The NestLink approach is a protein binder selection and identification technology able to biophysically characterize thousands of library members at once without handling individual clones at any stage of the process. Data were acquired on NGS and MS platforms at the Functional Genomics Center Zurich.
    """

    bioc = "NestLink"

    version("1.24.0", commit="886f69b0100fffe1832df82ccfaf4fd65f33f677")
    version("1.18.0", commit="23c3c6e97a9407eec4e96b10c2fe9e992f11a551")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-annotationhub@2.15:", type=("build", "run"))
    depends_on("r-experimenthub@1:", type=("build", "run"))
    depends_on("r-biostrings@2.51:", type=("build", "run"))
    depends_on("r-gplots@3:", type=("build", "run"))
    depends_on("r-protviz@0.4:", type=("build", "run"))
    depends_on("r-shortread@1.41:", type=("build", "run"))
