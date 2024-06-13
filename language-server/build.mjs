import { build } from 'esbuild';

build({
  entryPoints: ['src/cli.ts'],
  bundle: true,
  platform: 'node',
  target: 'node18',
  outfile: 'dist/cli.js',
  format: 'esm',
  external: ['@actions/languageserver'], // Mark this as external to avoid bundling issues
})
  .then(() => {
    console.log('Build completed');
  })
  .catch(() => process.exit(1));
