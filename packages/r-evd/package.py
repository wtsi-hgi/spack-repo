from spack.package import *


class REvd(RPackage):
    """Functions for extreme value distributions."""

    cran = "evd"

    version("2.3-6.1", sha256="662c592d3f5c5693dbf1c673d1137c4a60a347e330b71be1f3933f201d2c8971")

    depends_on("r", type=("build", "run"))

    # Fix build with R >= 4.4 where legacy Calloc/Free macros are missing
    def setup_build_environment(self, env):
        env.append_flags(
            "PKG_CPPFLAGS",
            "-include R_ext/RS.h -include R_ext/Memory.h -include spack_compat.h",
        )

    def patch(self):
        # Inject a small header that defines legacy allocation macros
        import os

        src_dir = os.path.join("src")
        os.makedirs(src_dir, exist_ok=True)
        compat_h = os.path.join(src_dir, "spack_compat.h")
        compat_contents = (
            "#ifndef SPACK_R_EVD_COMPAT_H\n"
            "#define SPACK_R_EVD_COMPAT_H\n"
            "#include <R.h>\n"
            "#include <R_ext/Memory.h>\n"
            "#ifndef Calloc\n"
            "#define Calloc(n,t) ((t*) R_chk_calloc((size_t)(n), sizeof(t)))\n"
            "#endif\n"
            "#ifndef Realloc\n"
            "#define Realloc(p,n,t) ((t*) R_chk_realloc((void*)(p), (size_t)(n) * sizeof(t)))\n"
            "#endif\n"
            "#ifndef Free\n"
            "#define Free(p) R_chk_free((void*)(p))\n"
            "#endif\n"
            "#endif /* SPACK_R_EVD_COMPAT_H */\n"
        )
        with open(compat_h, "w", encoding="utf-8") as f:
            f.write(compat_contents)
