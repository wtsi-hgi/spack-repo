# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenegeneinter(RPackage):
    """Tools for Testing Gene-Gene Interaction at the Gene Level

    The aim of this package is to propose several methods for testing gene-gene interaction in case-control association studies. Such a test can be done by aggregating SNP-SNP interaction tests performed at the SNP level (SSI) or by using gene-gene multidimensionnal methods (GGI) methods. The package also proposes tools for a graphic display of the results. <doi:10.18637/jss.v095.i12>.
    """

    bioc = "GeneGeneInteR"

    version("1.34.0", commit="9b29d5f9f317947e6569a0d66f973827e922695b")
    version("1.28.0", commit="5961a9fa0c9df843d1e719de1702239ed4473dd1")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-snpstats", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-kernlab", type=("build", "run"))
    depends_on("r-factominer", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))

    def patch(self):
        """Fix malformed DESCRIPTION fields that break R's DCF parser.

        Upstream 1.34.0 DESCRIPTION has two issues:
        - "Authors@R:" is appended to the end of the "Description:" line
        - Continuation lines (e.g., for Imports) are not indented

        R's read.dcf() requires that each field starts at column 1 and any
        continuation line starts with at least one leading space. This patch
        normalizes line endings, ensures a newline before "Authors@R:", and
        prefixes continuation lines with a single space when missing.
        """

        import os
        import re

        description_path = os.path.join(self.stage.source_path, "DESCRIPTION")

        if not os.path.exists(description_path):
            return

        # Read and normalize EOLs
        with open(description_path, "rb") as f:
            raw = f.read()

        normalized = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        text = normalized.decode("utf-8", errors="ignore")

        # Ensure Authors@R starts on its own line
        text = re.sub(r"(?<!\n)Authors@R:", "\nAuthors@R:", text)

        # Ensure continuation lines are indented
        fixed_lines = []
        previous_was_field = False
        field_header_re = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*:\s?")
        for line in text.split("\n"):
            if field_header_re.match(line):
                fixed_lines.append(line)
                previous_was_field = True
            else:
                # Non-header lines are continuations; indent if not already
                if line and not line.startswith(" "):
                    fixed_lines.append(" " + line)
                else:
                    fixed_lines.append(line)
                previous_was_field = False

        fixed_text = "\n".join(fixed_lines)

        with open(description_path, "w", encoding="utf-8") as f:
            f.write(fixed_text)
