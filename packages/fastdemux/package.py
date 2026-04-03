# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Fastdemux(CMakePackage):
    """fastdemux assigns single-cell libraries to donors using DLDA on
    barcoded BAM, VCF, and barcode inputs."""

    homepage = "https://github.com/piquelab/fastdemux"
    git = "https://github.com/piquelab/fastdemux.git"

    license = "MIT"

    version("20260210", commit="282e5df0dc6d283c3b1e8cb7b48b5acb97be96b1")

    depends_on("cmake@3.10:", type="build")
    depends_on("htslib@1.10:")
    depends_on("zlib")

    resource(
        name="klib",
        git="https://github.com/attractivechaos/klib.git",
        commit="97a0fcb790b43b9e5da8994f4671021fec036f19",
        destination=".",
        placement="klib",
    )

    def patch(self):
        spec = self.spec
        hts_include = spec["htslib"].headers.directories[0]
        hts_lib_dir = spec["htslib"].libs.directories[0]

        filter_file(
            "/wsu/el7/groups/piquelab/samtools/1.19/include",
            hts_include,
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            "/wsu/el7/groups/piquelab/samtools/1.19/lib",
            hts_lib_dir,
            "CMakeLists.txt",
            string=True,
        )
        filter_file(
            'set(CMAKE_INSTALL_PREFIX "/wsu/home/groups/piquelab/apps/el7/misc/")',
            "",
            "CMakeLists.txt",
            string=True,
        )

        help_blocks = {
            "fastdemux.c": """    if (help_requested) {
      fprintf(stderr, "Usage: %s [options] <BAM file> <VCF file> <Barcode file> <Output prefix>\\n", argv[0]);
      fprintf(stderr, "Options:\\n");
      fprintf(stderr, " -q, --min-qual-score NUM  Minimum quality score (default: %d)\\n",min_qual_score);
      fprintf(stderr, " -b, --min-base-qual NUM   Minimum base quality (default: %d)\\n",min_base_qual);
      fprintf(stderr, " --max-var REAL  Threshold on max 2*q*(1-q) to select more informative SNPs  (default: %f)\\n",max_var);
      fprintf(stderr, " --max-snps NUM  Max number of SNPs  (useful for debug, default: %d All)\\n",max_snps);
      fprintf(stderr, " -t, --num-threads NUM  Number of OpenMP threads (default: %d)\\n",num_threads);
      return 0;
    }

    // Check for required files and other positional arguments if necessary""",
            "fastaseq.c": """    if (help_requested) {
      fprintf(stderr, "Usage: %s [options] <BAM file> <VCF file> <Barcode file> <Output prefix>\\n", argv[0]);
      fprintf(stderr, "Options:\\n");
      fprintf(stderr, " -q, --min-qual-score NUM  Minimum quality score (default: %d)\\n",min_qual_score);
      fprintf(stderr, " -b, --min-base-qual NUM   Minimum base quality (default: %d)\\n",min_base_qual);
      fprintf(stderr, " --min-het-prob REAL Minimum probability to consider a heterozygote  (default: %f)\\n",min_het_prob);
      fprintf(stderr, " --max-snps NUM  Max number of SNPs  (useful for debug, default: %d All)\\n",max_snps);
      fprintf(stderr, " -t, --num-threads NUM  Number of OpenMP threads (default: %d)\\n",num_threads);
      return 0;
    }

    // Check for required files and other positional arguments if necessary""",
        }

        for source in ("fastdemux.c", "fastaseq.c"):
            filter_file(
                'while ((c = ketopt(&opt, argc, argv, 1, "q:b:t:", longopts)) >= 0) {',
                'while ((c = ketopt(&opt, argc, argv, 1, "hq:b:t:", longopts)) >= 0) {',
                source,
                string=True,
            )
            filter_file(
                "int c, min_qual_score = 20, min_base_qual = 13, num_threads = OMP_THREADS, max_snps=0; // default values",
                "int c, min_qual_score = 20, min_base_qual = 13, num_threads = OMP_THREADS, max_snps=0; // default values\n    int help_requested = 0;",
                source,
                string=True,
            )
            filter_file(
                "      case '?':",
                "      case 'h':\n        help_requested = 1;\n\tbreak;\n      case '?':",
                source,
                string=True,
            )
            filter_file(
                "    // Check for required files and other positional arguments if necessary",
                help_blocks[source],
                source,
                string=True,
            )

    @run_after("install")
    def install_test(self):
        """Run lightweight CLI smoke tests."""
        fastdemux = Executable(join_path(self.prefix.bin, "fastdemux"))
        fastaseq = Executable(join_path(self.prefix.bin, "fastaseq"))
        fastdemux("-h")
        fastaseq("-h")
