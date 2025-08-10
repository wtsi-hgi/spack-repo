# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class RShortread(RPackage):
    """FASTQ input and manipulation.

    This package implements sampling, iteration, and input of FASTQ files.
    The package includes functions for filtering and trimming reads, and for
    generating a quality assessment report. Data are represented as
    DNAStringSet-derived objects, and easily manipulated for a diversity of
    purposes. The package also contains legacy support for early single-end,
    ungapped alignment formats."""

    bioc = "ShortRead"
    version("1.66.0", commit="2363c083d3435760f7228bc49c931bc801675480")
    version("1.60.0", commit="4304db40717b0b7c46f7f7a4b78796ae916c1485")
    version("1.58.0", commit="433d18266b141ddcc9dc590f5244163a04efebe3")
    version("1.56.0", commit="df25d0872d52aac3610998abda0d7bfd37298726")
    version("1.54.0", commit="a1082a335120860d019aa0065a975d41890351f7")
    version("1.52.0", commit="4d7304d7b5a0ca5c904c0b919d6c95599db72a39")
    version("1.48.0", commit="ba44cd2517bc0e6f46d2cfcfce393f86eec814d0")
    version("1.42.0", commit="daa2576a48278460caf87f42c022c796652f4908")
    version("1.40.0", commit="0cbe4b62b0be4c5f2e2670da17493423446e008f")
    version("1.38.0", commit="e9498f04b7b4bf0212bbb10ec7e3de2d7699f4bf")
    version("1.36.1", commit="176c34eddf4a416d30c69cb4ac197141ba42e66f")
    version("1.34.2", commit="25daac63b301df66a8ef6e98cc2977522c6786cd")

    depends_on("r-biocgenerics@0.23.3:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
    depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
    depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
    depends_on("r-hwriter", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-latticeextra", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-rhtslib", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
    # Note: The archived CRAN package 'pwalign' is not reliably fetchable
    # anymore from CRAN mirrors. We remove it from ShortRead's DESCRIPTION
    # during patching to allow installation and basic usage.

    def patch(self):
        # Robustly rewrite Imports line in DESCRIPTION to remove 'pwalign'
        desc_path = "DESCRIPTION"
        if os.path.exists(desc_path):
            with open(desc_path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            new_lines = []
            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("Imports:"):
                    imports_payload = line[len("Imports:"):].strip()
                    i += 1
                    while i < len(lines) and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                        imports_payload += " " + lines[i].strip()
                        i += 1
                    tokens = [t.strip() for t in imports_payload.split(",")]
                    tokens = [t for t in tokens if t and t != "pwalign"]
                    rebuilt = "Imports: " + ", ".join(tokens)
                    new_lines.append(rebuilt)
                    continue
                new_lines.append(line)
                i += 1
            with open(desc_path, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines) + "\n")
        # Remove any import directives for pwalign in NAMESPACE and ensure Biostrings imports
        ns_path = "NAMESPACE"
        if os.path.exists(ns_path):
            with open(ns_path, "r", encoding="utf-8") as f:
                ns_lines = f.read().splitlines()
            # Drop all lines that reference pwalign in any way
            ns_lines = [ln for ln in ns_lines if "pwalign" not in ln]
            # Ensure necessary Biostrings imports are present
            ensure_lines = [
                "importFrom(Biostrings, pairwiseAlignment)",
                "importFrom(Biostrings, unaligned)",
            ]
            for needed in ensure_lines:
                if not any(ln.strip() == needed for ln in ns_lines):
                    ns_lines.append(needed)
            with open(ns_path, "w", encoding="utf-8") as f:
                f.write("\n".join(ns_lines) + "\n")

        # Ensure generics for pairwiseAlignment and unaligned exist before setMethod calls
        # by prepending to relevant R source files if needed
        generic_block = (
            "if (!isGeneric(\"pairwiseAlignment\")) {\n"
            "    setGeneric(\"pairwiseAlignment\", function(pattern, subject, ...) standardGeneric(\"pairwiseAlignment\"))\n"
            "}\n"
            "if (!isGeneric(\"unaligned\")) {\n"
            "    setGeneric(\"unaligned\", function(x, ...) standardGeneric(\"unaligned\"))\n"
            "}\n"
        )
        r_files = [
            os.path.join("R", "methods-ShortRead.R"),
            os.path.join("R", "methods-ShortReadQ.R"),
        ]
        for r_path in r_files:
            if os.path.exists(r_path):
                with open(r_path, "r", encoding="utf-8") as f:
                    content = f.read()
                if "setMethod(pairwiseAlignment" in content and "setGeneric(\"pairwiseAlignment\")" not in content:
                    content = generic_block + "\n" + content
                    with open(r_path, "w", encoding="utf-8") as f:
                        f.write(content)
