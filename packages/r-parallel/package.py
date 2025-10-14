from spack.package import *


class RParallel(Package):
    """R's base 'parallel' package (ships with R).

    This is a meta-package to express dependencies on R's built-in
    'parallel' package. It does not install any code itself; instead it
    requires a compatible version of R which already includes 'parallel'.
    """

    homepage = "https://www.rdocumentation.org/packages/parallel/versions/3.6.2"
    has_code = False

    # Version aligns with the R release that contains this package version.
    version("3.6.2")

    # 'parallel' is included with R since 2.14.0; for 3.6.2 specifically
    # ensure an R toolchain of at least that version is present.
    depends_on("r@3.6.2:", type=("build", "run"))

    def install(self, spec, prefix):
        # Create a minimal marker so Spack records an installation.
        mkdirp(prefix)
        with open(join_path(prefix, ".spack-r-parallel"), "w") as f:
            f.write("meta-package for R's base 'parallel'\n")
