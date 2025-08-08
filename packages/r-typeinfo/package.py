# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
import shutil


class RTypeinfo(RPackage):
    """Optional Type Specification Prototype

    A prototype for a mechanism for specifying the types of parameters and the return value for an R function. This is meta-information that can be used to generate stubs for servers and various interfaces to these functions. Additionally, the arguments in a call to a typed function can be validated using the type specifications. We allow types to be specified as either i) by class name using either inheritance - is(x, className), or strict instance of - class(x) %in% className, or ii) a dynamic test given as an R expression which is evaluated at run-time. More precise information and interesting tests can be done via ii), but it is harder to use this information as meta-data as it requires more effort to interpret it and it is of course run-time information. It is typically more meaningful.
    """

    bioc = "TypeInfo"

    version("1.74.0", commit="c3cf335ad1987d8e7cf5e7e8a3d5a4e3ac9a6bfb")
    version("1.68.0", commit="8933d6dfe64af946a15c0f50a98916c7c7444827")

    def patch(self):
        # Normalize file names and Collate to use zzz.S consistently
        # 1) Ensure DESCRIPTION Collate lists zzz.S
        desc_path = os.path.join("DESCRIPTION")
        if os.path.exists(desc_path):
            filter_file(r"zzz\\.R", "zzz.S", desc_path)
            # And normalize the entire Collate line to the expected set
            with open(desc_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                if line.startswith("Collate:"):
                    new_lines.append(
                        "Collate: Classes.S checkArgs.S print.S rewrite.S support.S zzz.S\n"
                    )
                else:
                    new_lines.append(line)
            with open(desc_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

        # 2) Ensure there is only zzz.S in R/, not zzz.R
        r_dir = os.path.join("R")
        zr = os.path.join(r_dir, "zzz.R")
        zs = os.path.join(r_dir, "zzz.S")
        if os.path.exists(zr):
            # If zzz.S does not exist, rename; if it exists, remove zzz.R
            if not os.path.exists(zs):
                os.rename(zr, zs)
            else:
                os.remove(zr)
