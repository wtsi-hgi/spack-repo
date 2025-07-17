# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSradb(RPackage):
    """A compilation of metadata from NCBI SRA and tools

    The Sequence Read Archive (SRA) is the largest public repository of sequencing data from the next generation of sequencing platforms including Roche 454 GS System, Illumina Genome Analyzer, Applied Biosystems SOLiD System, Helicos Heliscope, and others. However, finding data of interest can be challenging using current tools. SRAdb is an attempt to make access to the metadata associated with submission, study, sample, experiment and run much more feasible. This is accomplished by parsing all the NCBI SRA metadata into a SQLite database that can be stored and queried locally. Fulltext search in the package make querying metadata very flexible and powerful.  fastq and sra files can be downloaded for doing alignment locally. Beside ftp protocol, the SRAdb has funcitons supporting fastp protocol (ascp from Aspera Connect) for faster downloading large data files over long distance. The SQLite database is updated regularly as new data is added to SRA and can be downloaded at will for the most up-to-date metadata.
    """

    bioc = "SRAdb"

    version("1.70.0", commit="0ea2915be015cbad1f789f681182594a9a0fc1b3")
    version("1.64.0", commit="4bf61b79c0067c9f38691fed4d961fcae658e24e")

    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-geoquery", type=("build", "run"))
